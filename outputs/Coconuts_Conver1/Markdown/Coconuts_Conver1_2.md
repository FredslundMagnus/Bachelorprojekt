
# Parameters

    Name :                      Coconuts_Conver1-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63387931145 function calls (63077838130 primitive calls) in 86108.78 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.775 86108.775 {built-in method builtins.exec}
                      1    4.597    4.597 86108.775 86108.775 <string>:1(<module>)
                      1  365.807  365.807 86104.178 86104.178 main.py:79(CFagent)
               10433253   41.644    0.000 32722.652    0.003 agent.py:29(learn)
               10433251  807.875    0.000 27335.626    0.003 learner.py:42(Qlearn)
                3477751   15.512    0.000 19064.396    0.005 game.py:41(step)
                3477751   19.229    0.000 18290.275    0.005 layers.py:718(step)
        347524769/37433445 1472.488    0.000 13406.988    0.000 module.py:866(_call_impl)
                3477751  357.429    0.000 12612.241    0.004 agent.py:54(_learn)
               27000194   78.172    0.000 12555.438    0.000 network.py:27(forward)
                3477751  318.615    0.000 12418.143    0.004 layers.py:17(step)
               27000194  384.360    0.000 12300.135    0.000 container.py:117(forward)
              347550396 1235.182    0.000 12069.385    0.000 layer.py:98(move)
                3477751  354.019    0.000 11694.525    0.003 agent.py:204(_learn)
               10433251   92.857    0.000 11650.154    0.001 optimizer.py:84(wrapper)
               10433251   44.627    0.000 11209.356    0.001 grad_mode.py:24(decorate_context)
               10433251  316.614    0.000 11061.141    0.001 adam.py:55(step)
               10433251 2279.370    0.000 10396.728    0.001 _functional.py:53(adam)
                3477751  107.657    0.000 8345.047    0.002 agent.py:117(_learn)
              347550396 1265.825    0.000 7403.665    0.000 layers.py:735(check)
               10433251   45.279    0.000 6808.338    0.001 tensor.py:195(backward)
               10433251   41.223    0.000 6761.453    0.001 __init__.py:68(backward)
                3477751  573.514    0.000 6744.163    0.002 agent.py:212(counterfact)
               10433251 6476.845    0.001 6476.845    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8276752  227.496    0.000 6241.630    0.001 agent.py:49(__call__)
                3477752  501.691    0.000 5826.967    0.002 layers.py:684(update)
                3477751 4147.916    0.001 5298.827    0.002 replaybuffer.py:22(sample_data)
                3477751 3940.482    0.001 5057.294    0.001 replaybuffer.py:67(sample_data)
                3477751 2383.074    0.001 4987.167    0.001 agent.py:88(interveen)
                3477751 2469.582    0.001 4687.265    0.001 replaybuffer.py:28(teleporter_save_data)
               54000388  121.412    0.000 4412.411    0.000 conv.py:398(forward)
               54000388   75.561    0.000 4235.964    0.000 conv.py:390(_conv_forward)
               54000388 4160.404    0.000 4160.404    0.000 {built-in method conv2d}
               74045080  156.198    0.000 3575.100    0.000 linear.py:93(forward)
               42663846 3523.103    0.000 3523.103    0.000 {built-in method tensor}
               74045080   63.791    0.000 3345.243    0.000 functional.py:1737(linear)
               34674546   24.075    0.000 3280.649    0.000 game.py:37(board)
               74045080 3265.654    0.000 3265.654    0.000 {built-in method torch._C._nn.linear}
               48688521 1855.138    0.000 3129.402    0.000 layer.py:151(update)
                3477751 2014.700    0.001 3061.231    0.001 agent.py:67(modify)
              347550396  527.485    0.000 2580.234    0.000 layers.py:729(isFree)
              347550396 1619.223    0.000 2282.358    0.000 layers.py:471(check)
              194754016 2122.292    0.000 2122.292    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2315400179 1672.494    0.000 2052.748    0.000 layer.py:95(isFree)
              147287142 2023.028    0.000 2023.028    0.000 {built-in method clone}
                1334691   30.759    0.000 2015.799    0.002 agent.py:176(choose_action)
              101045274   84.026    0.000 2009.273    0.000 activation.py:713(forward)
               46532003 1967.279    0.000 1967.279    0.000 {built-in method cat}
              101045274   90.155    0.000 1925.248    0.000 functional.py:1364(leaky_relu)
              347550396 1345.199    0.000 1877.037    0.000 layers.py:77(check)
              194754016 1872.057    0.000 1872.057    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3477749   59.936    0.000 1823.015    0.001 agent.py:172(__call__)
              101045274 1817.193    0.000 1817.193    0.000 {built-in method torch._C._nn.leaky_relu}
               11754503   83.140    0.000 1768.474    0.000 agent.py:59(modify_board)
                3477751   57.631    0.000 1698.045    0.000 agent.py:112(__call__)
               10433251  254.329    0.000 1602.335    0.000 optimizer.py:189(zero_grad)
             5944073705 1070.774    0.000 1535.782    0.000 enum.py:646(__hash__)
                2040097   22.601    0.000 1471.797    0.001 layers.py:740(restart)
                2040097   12.558    0.000 1238.566    0.001 level.py:8(__init__)
               97377008 1163.125    0.000 1163.125    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              349212855  284.095    0.000 1154.717    0.000 {built-in method builtins.any}
                3477751  918.623    0.000 1140.033    0.000 replaybuffer.py:73(CF_save_data)
                2040097   84.068    0.000 1133.570    0.001 levels.py:262(generate)
               11754503 1119.131    0.000 1119.131    0.000 {built-in method torch._C._nn.one_hot}
               97377008 1009.625    0.000 1009.625    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               18191832  165.898    0.000  978.154    0.000 level.py:41(notUsed)
               97377008  965.234    0.000  965.234    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               97377008  955.387    0.000  955.387    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3477751   67.893    0.000  898.504    0.000 replaybuffer.py:18(stacker)
              347550396  671.293    0.000  885.862    0.000 layers.py:62(check)
                3477749   65.547    0.000  873.336    0.000 replaybuffer.py:63(stacker)
             2765880824  703.386    0.000  870.623    0.000 layers.py:700(<genexpr>)
              347775200   84.987    0.000  794.372    0.000 {built-in method builtins.all}
              707569390  156.184    0.000  755.314    0.000 layers.py:690(<genexpr>)
             8136644010  752.343    0.000  752.343    0.000 layer.py:91(positions)
                3477751  454.939    0.000  750.816    0.000 collector.py:46(collect)
               97377008  741.160    0.000  741.160    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1042999397  702.597    0.000  702.597    0.000 layer.py:146(elements)
                8276752  236.483    0.000  645.440    0.000 exploration.py:53(softmaxer)
              347775200  392.436    0.000  594.511    0.000 layers.py:113(isDone)
              681639140  468.776    0.000  581.781    0.000 tensor.py:906(grad)
        7092419806/7092419803  510.752    0.000  579.884    0.000 {built-in method builtins.len}
               10433251   15.365    0.000  529.893    0.000 loss.py:527(forward)
              162519394  528.517    0.000  528.517    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               10433251   39.864    0.000  514.528    0.000 functional.py:2898(mse_loss)
                6955502  180.581    0.000  482.549    0.000 random.py:315(sample)
              347550396  306.976    0.000  466.237    0.000 layers.py:48(check)
             5944113272  465.015    0.000  465.015    0.000 {built-in method builtins.hash}
               18191832   17.621    0.000  437.199    0.000 level.py:38(elementsIn)
              347550396  252.179    0.000  368.154    0.000 layers.py:23(check)
               10433251  340.389    0.000  340.389    0.000 {built-in method torch._C._nn.mse_loss}
               54000388   39.263    0.000  331.131    0.000 flatten.py:39(forward)
              354186969  217.599    0.000  329.081    0.000 layer.py:126(remove)
               20866506  315.557    0.000  315.557    0.000 {built-in method sum}
                6955504  301.906    0.000  301.906    0.000 {built-in method nonzero}
               10434425  298.513    0.000  298.513    0.000 {built-in method max}
               54000388  291.868    0.000  291.868    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1334691  291.318    0.000  291.318    0.000 agent.py:187(convert_values)
               18191832  139.309    0.000  277.885    0.000 level.py:39(<listcomp>)
             2315400179  263.294    0.000  263.294    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579168: <Coconuts_Conver1_2> in cluster <dcc> Done

Job <Coconuts_Conver1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:31:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:31:48 2021
Terminated at Fri Apr 30 10:27:02 2021
Results reported at Fri Apr 30 10:27:02 2021

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

    CPU time :                                   85896.38 sec.
    Max Memory :                                 9848 MB
    Average Memory :                             6570.69 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6536.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            286975 sec.

The output (if any) is above this job summary.

