
# Parameters

    Name :                      Causal4_Cf_convert3_TopN3-2
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      62565068694 function calls (62283415075 primitive calls) in 86111.44 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.439 86111.439 {built-in method builtins.exec}
                      1    5.467    5.467 86111.439 86111.439 <string>:1(<module>)
                      1  364.279  364.279 86105.972 86105.972 main.py:79(CFagent)
                9163845   33.553    0.000 30462.991    0.003 agent.py:29(learn)
                9163834  757.005    0.000 25360.500    0.003 learner.py:42(Qlearn)
                3054615   16.312    0.000 19054.538    0.006 game.py:41(step)
                3054615   19.638    0.000 18261.783    0.006 layers.py:718(step)
        315304961/33653033 1378.762    0.000 12902.050    0.000 module.py:866(_call_impl)
                3054615  280.549    0.000 12547.507    0.004 layers.py:17(step)
              305210807  896.610    0.000 12236.531    0.000 layer.py:98(move)
               24489199   73.776    0.000 12111.353    0.000 network.py:27(forward)
               24489199  371.372    0.000 11878.289    0.000 container.py:117(forward)
                3054615  377.789    0.000 11762.719    0.004 agent.py:54(_learn)
                3054615  374.891    0.000 10909.427    0.004 agent.py:202(_learn)
                9163834   83.253    0.000 10766.761    0.001 optimizer.py:84(wrapper)
                9163834   40.240    0.000 10362.900    0.001 grad_mode.py:24(decorate_context)
                9163834  291.264    0.000 10229.900    0.001 adam.py:55(step)
                3054615  934.519    0.000 9948.397    0.003 agent.py:210(counterfact)
                9163834 2101.106    0.000 9616.997    0.001 _functional.py:53(adam)
                3054615  103.271    0.000 7735.843    0.003 agent.py:117(_learn)
              305210807 1447.052    0.000 7526.133    0.000 layers.py:735(check)
                9163834   40.627    0.000 6304.081    0.001 tensor.py:195(backward)
                9163834   37.439    0.000 6261.863    0.001 __init__.py:68(backward)
                7658116  226.821    0.000 6116.826    0.001 agent.py:49(__call__)
                9163834 5997.585    0.001 5997.585    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3054616  461.745    0.000 5668.740    0.002 layers.py:684(update)
                3054615 4298.769    0.001 5498.241    0.002 replaybuffer.py:22(sample_data)
                3054615 4096.363    0.001 5231.993    0.002 replaybuffer.py:67(sample_data)
               48128274 5231.120    0.000 5231.120    0.000 {built-in method tensor}
               41071257   28.706    0.000 5007.048    0.000 game.py:37(board)
                3054615 2014.538    0.001 4437.325    0.001 agent.py:88(interveen)
               48978398  117.421    0.000 4295.118    0.000 conv.py:398(forward)
               48978398   70.448    0.000 4124.287    0.000 conv.py:390(_conv_forward)
               48978398 4053.838    0.000 4053.838    0.000 {built-in method conv2d}
               61092310 2341.017    0.000 4022.950    0.000 layer.py:151(update)
                3054615 2134.838    0.001 3990.681    0.001 replaybuffer.py:28(teleporter_save_data)
               67358367  145.627    0.000 3466.341    0.000 linear.py:93(forward)
               67358367   59.382    0.000 3250.920    0.000 functional.py:1737(linear)
              305210807  646.491    0.000 3192.801    0.000 layers.py:729(isFree)
               67358367 3176.198    0.000 3176.198    0.000 {built-in method torch._C._nn.linear}
                3054615 1923.890    0.001 2900.202    0.001 agent.py:67(modify)
                1558030   39.930    0.000 2599.314    0.002 agent.py:175(choose_action)
             2892896079 2083.131    0.000 2546.311    0.000 layer.py:95(isFree)
               41258826 2062.021    0.000 2062.021    0.000 {built-in method cat}
              171058220 1987.249    0.000 1987.249    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               91847566   80.203    0.000 1931.131    0.000 activation.py:713(forward)
               91847566   81.655    0.000 1850.928    0.000 functional.py:1364(leaky_relu)
              121909290 1788.869    0.000 1788.869    0.000 {built-in method clone}
               91847566 1751.101    0.000 1751.101    0.000 {built-in method torch._C._nn.leaky_relu}
              171058220 1737.283    0.000 1737.283    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3054604   59.712    0.000 1702.074    0.001 agent.py:171(__call__)
               10712731   78.223    0.000 1698.104    0.000 agent.py:59(modify_board)
                3054615   56.069    0.000 1581.629    0.001 agent.py:112(__call__)
             5710822003 1094.222    0.000 1571.685    0.000 enum.py:646(__hash__)
                9163834  236.055    0.000 1475.818    0.000 optimizer.py:189(zero_grad)
              305658369  334.005    0.000 1428.081    0.000 {built-in method builtins.any}
                3054615 1068.456    0.000 1373.552    0.000 replaybuffer.py:73(CF_save_data)
              305210807  900.155    0.000 1195.660    0.000 layers.py:77(check)
                2857847   38.338    0.000 1110.024    0.000 layers.py:740(restart)
             3328641283  899.508    0.000 1094.076    0.000 layers.py:700(<genexpr>)
               10712731 1075.671    0.000 1075.671    0.000 {built-in method torch._C._nn.one_hot}
               85529110 1074.750    0.000 1074.750    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              305210807  679.153    0.000 1065.614    0.000 layers.py:246(check)
              305210807  596.594    0.000  985.232    0.000 layers.py:286(check)
                3054615   63.872    0.000  963.683    0.000 replaybuffer.py:18(stacker)
              996125220  929.703    0.000  929.703    0.000 layer.py:146(elements)
               85529110  929.513    0.000  929.513    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3054604   64.121    0.000  905.461    0.000 replaybuffer.py:63(stacker)
               85529110  886.344    0.000  886.344    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85529110  873.186    0.000  873.186    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2857847   17.761    0.000  782.459    0.000 level.py:8(__init__)
             7469624757  709.636    0.000  709.636    0.000 layer.py:91(positions)
                3054615  419.669    0.000  696.501    0.000 collector.py:46(collect)
               85529110  684.957    0.000  684.957    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              305210807  490.520    0.000  641.531    0.000 layers.py:62(check)
        8086703065/8086703062  573.641    0.000  637.159    0.000 {built-in method builtins.len}
                7658116  229.929    0.000  630.535    0.000 exploration.py:53(softmaxer)
                2857847  101.565    0.000  625.675    0.000 levels.py:199(generate)
              305210807  356.659    0.000  555.230    0.000 layers.py:313(check)
              598703854  426.227    0.000  531.143    0.000 tensor.py:906(grad)
              305210807  327.856    0.000  514.424    0.000 layers.py:273(check)
               11824924  189.624    0.000  501.325    0.000 random.py:315(sample)
                9163834   14.359    0.000  491.532    0.000 loss.py:527(forward)
              135676625  478.887    0.000  478.887    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             5710856866  477.471    0.000  477.471    0.000 {built-in method builtins.hash}
                9163834   39.192    0.000  477.172    0.000 functional.py:2898(mse_loss)
              305210807  307.313    0.000  456.748    0.000 layers.py:48(check)
                1558030  430.106    0.000  455.649    0.000 agent.py:186(convert_values)
                5715694   49.689    0.000  425.711    0.000 level.py:41(notUsed)
              305461600   64.765    0.000  417.075    0.000 {built-in method builtins.all}
              665510526  159.508    0.000  391.375    0.000 layers.py:690(<genexpr>)
              305210807  233.861    0.000  349.648    0.000 layers.py:23(check)
               48978398   34.980    0.000  318.449    0.000 flatten.py:39(forward)
                9163834  316.901    0.000  316.901    0.000 {built-in method torch._C._nn.mse_loss}
               18327690  295.279    0.000  295.279    0.000 {built-in method sum}
              267591909  209.920    0.000  284.909    0.000 layer.py:126(remove)
             3369197726  284.518    0.000  284.518    0.000 {method 'random' of '_random.Random' objects}
                9164904  283.794    0.000  283.794    0.000 {built-in method max}
               48978398  283.469    0.000  283.469    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6109232  283.459    0.000  283.459    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551817: <Causal4_Cf_convert3_TopN3_2> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 05:05:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 05:05:50 2021
Terminated at Fri Apr 23 05:01:07 2021
Results reported at Fri Apr 23 05:01:07 2021

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

    CPU time :                                   85903.84 sec.
    Max Memory :                                 8964 MB
    Average Memory :                             6088.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7420.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            178836 sec.

The output (if any) is above this job summary.

