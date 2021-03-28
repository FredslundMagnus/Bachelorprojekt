
# Parameters

    Name :                      causal1_good-0
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     20.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1195 minutes.
    Hours used :                19 hours.

# Profiling


      54890758199 function calls (54670153236 primitive calls) in 71710.72 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71710.723 71710.723 {built-in method builtins.exec}
                      1    1.896    1.896 71710.723 71710.723 <string>:1(<module>)
                      1  178.805  178.805 71708.826 71708.826 main.py:43(teleport)
                7879154   28.765    0.000 22320.963    0.003 agent.py:27(learn)
                7879154  576.614    0.000 18954.802    0.002 learner.py:42(Qlearn)
                3939577   17.020    0.000 15746.881    0.004 game.py:27(step)
                3939577   21.317    0.000 14875.679    0.004 layers.py:475(step)
                3939577 7704.180    0.002 14001.108    0.004 replaybuffer.py:29(teleporter_save_data)
                3939577  380.732    0.000 13430.472    0.003 agent.py:52(_learn)
        248179961/27576009 1013.569    0.000 8923.049    0.000 module.py:866(_call_impl)
                3939577  101.534    0.000 8846.147    0.002 agent.py:113(_learn)
                3939577 5842.747    0.001 8571.546    0.002 agent.py:84(interveen)
                3939577  299.958    0.000 8392.815    0.002 layers.py:18(step)
               19696855   55.282    0.000 8292.645    0.000 network.py:24(forward)
               19696855  255.249    0.000 8111.905    0.000 container.py:117(forward)
              393957700  485.530    0.000 8060.779    0.000 layer.py:76(move)
                7879154   69.056    0.000 7913.242    0.001 optimizer.py:84(wrapper)
                7879154   33.587    0.000 7593.679    0.001 grad_mode.py:24(decorate_context)
                7879154  222.240    0.000 7485.665    0.001 adam.py:55(step)
                7879154 1535.459    0.000 7008.540    0.001 _functional.py:53(adam)
                3939578  395.800    0.000 6434.393    0.002 layers.py:446(update)
                7878124  177.496    0.000 5546.883    0.001 agent.py:47(__call__)
              434110880 5093.807    0.000 5093.807    0.000 {built-in method clone}
                7879154   38.011    0.000 4851.862    0.001 tensor.py:195(backward)
                7879154   31.747    0.000 4812.637    0.001 __init__.py:68(backward)
                3939577 3332.143    0.001 4667.147    0.001 replaybuffer.py:23(sample_data)
                7879154 4607.317    0.001 4607.317    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              393957700  826.797    0.000 4591.712    0.000 layers.py:492(check)
                3939577 2017.795    0.001 3193.126    0.001 agent.py:65(modify)
               39393710   88.396    0.000 2972.658    0.000 conv.py:398(forward)
               39393710   48.341    0.000 2845.017    0.000 conv.py:390(_conv_forward)
               13734089  111.359    0.000 2828.214    0.000 layers.py:496(restart)
               39393710 2796.676    0.000 2796.676    0.000 {built-in method conv2d}
              393957700  566.796    0.000 2483.491    0.000 layers.py:486(isFree)
               51211411  105.447    0.000 2303.561    0.000 linear.py:93(forward)
               51211411   41.756    0.000 2141.670    0.000 functional.py:1737(linear)
               51211411 2089.747    0.000 2089.747    0.000 {built-in method torch._C._nn.linear}
               31516624 1170.217    0.000 2039.275    0.000 layer.py:137(NoRock_update)
             3063911266 1528.310    0.000 1916.695    0.000 layer.py:73(isFree)
               13734089   53.417    0.000 1823.292    0.000 level.py:8(__init__)
                3939577   52.419    0.000 1761.878    0.000 agent.py:108(__call__)
               11817701   80.105    0.000 1685.570    0.000 agent.py:57(modify_board)
               13734089   98.537    0.000 1543.899    0.000 levels.py:122(generate)
              141824772 1418.777    0.000 1418.777    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             6058326575  982.353    0.000 1386.669    0.000 enum.py:646(__hash__)
               41202267  306.346    0.000 1345.801    0.000 level.py:41(notUsed)
               35455163 1339.896    0.000 1339.896    0.000 {built-in method cat}
              445928581 1316.100    0.000 1316.100    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               70908266   56.181    0.000 1285.719    0.000 activation.py:713(forward)
              141824772 1252.364    0.000 1252.364    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16879626 1236.162    0.000 1236.162    0.000 {built-in method tensor}
               70908266   57.695    0.000 1229.538    0.000 functional.py:1364(leaky_relu)
               70908266 1160.498    0.000 1160.498    0.000 {built-in method torch._C._nn.leaky_relu}
                7879154  180.545    0.000 1117.723    0.000 optimizer.py:189(zero_grad)
               11817701 1080.574    0.000 1080.574    0.000 {built-in method torch._C._nn.one_hot}
                3939577   73.017    0.000 1062.747    0.000 replaybuffer.py:19(stacker)
              393957800  115.783    0.000 1021.291    0.000 {built-in method builtins.all}
              393957700  615.185    0.000  984.221    0.000 layers.py:302(check)
                7879154    8.872    0.000  964.345    0.000 game.py:23(board)
             1267592343  291.246    0.000  948.981    0.000 layers.py:452(<genexpr>)
              393957700  571.428    0.000  930.233    0.000 layers.py:261(check)
              109872712   79.292    0.000  858.244    0.000 layer.py:50(restart)
               70912386  803.914    0.000  803.914    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3939577  475.089    0.000  795.233    0.000 collector.py:54(collect)
               70912386  682.595    0.000  682.595    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               70912386  650.411    0.000  650.411    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13734189  324.602    0.000  649.871    0.000 layers.py:33(reset)
               70912386  644.489    0.000  644.489    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              393957700  412.386    0.000  640.135    0.000 layers.py:328(check)
              393957800  406.008    0.000  611.083    0.000 layers.py:110(isDone)
              393957700  383.595    0.000  595.051    0.000 layers.py:287(check)
                7878124  209.764    0.000  581.288    0.000 exploration.py:53(softmaxer)
             6331019343  564.961    0.000  564.961    0.000 layer.py:69(positions)
             1770826613  556.921    0.000  556.921    0.000 layer.py:116(elements)
              393957700  331.675    0.000  522.884    0.000 layers.py:47(check)
               41202267   28.952    0.000  509.211    0.000 level.py:38(elementsIn)
               70912386  505.930    0.000  505.930    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              860745687  316.731    0.000  439.806    0.000 layer.py:100(add)
              496386756  341.930    0.000  422.349    0.000 tensor.py:906(grad)
             6058355270  404.320    0.000  404.320    0.000 {built-in method builtins.hash}
                7879154   11.183    0.000  385.750    0.000 loss.py:527(forward)
                7879154   30.759    0.000  374.567    0.000 functional.py:2898(mse_loss)
             2021656215  368.944    0.000  368.944    0.000 level.py:32(inverse)
               23637462  336.315    0.000  336.315    0.000 {built-in method sum}
        3540801997/3540801995  270.539    0.000  329.479    0.000 {built-in method builtins.len}
               41202267  156.659    0.000  312.314    0.000 level.py:39(<listcomp>)
              393613194  200.826    0.000  288.886    0.000 layer.py:96(remove)
                3939577   97.235    0.000  265.020    0.000 random.py:315(sample)
                7879154  245.076    0.000  245.076    0.000 {built-in method torch._C._nn.mse_loss}
               39393710   32.132    0.000  226.596    0.000 flatten.py:39(forward)
               11818731   19.490    0.000  216.142    0.000 tensor.py:525(__rsub__)
             2301067390  213.843    0.000  213.843    0.000 layer.py:177(isBlocking)
                7880334  213.390    0.000  213.390    0.000 {built-in method max}
                3939577   16.845    0.000  212.127    0.000 exploration.py:47(epsilonGreedy)
               39393710  194.464    0.000  194.464    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11818731  193.723    0.000  193.723    0.000 {built-in method rsub}
               13734089   87.119    0.000  192.975    0.000 level.py:16(<dictcomp>)
             2517457977  192.135    0.000  192.135    0.000 {method 'append' of 'list' objects}
                7878124  188.278    0.000  188.278    0.000 {built-in method multinomial}
             1043790771  181.106    0.000  181.106    0.000 enum.py:352(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9474221: <causal1_good_0> in cluster <dcc> Done

Job <causal1_good_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 27 17:45:03 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 17:45:04 2021
Terminated at Sun Mar 28 14:40:21 2021
Results reported at Sun Mar 28 14:40:21 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   71682.01 sec.
    Max Memory :                                 3025 MB
    Average Memory :                             3022.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13359.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71734 sec.
    Turnaround time :                            71718 sec.

The output (if any) is above this job summary.

