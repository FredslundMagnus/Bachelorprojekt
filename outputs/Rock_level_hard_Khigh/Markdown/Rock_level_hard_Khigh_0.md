
# Parameters

    Name :                      Rock_level_hard_Khigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     11.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         1000000.0
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      38425921839 function calls (38286365616 primitive calls) in 39315.16 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.158 39315.158 {built-in method builtins.exec}
                      1    0.912    0.912 39315.158 39315.158 <string>:1(<module>)
                      1   98.764   98.764 39314.246 39314.246 main.py:13(teleport)
                2492184    8.247    0.000 15617.934    0.006 game.py:27(step)
                2492184   10.857    0.000 15095.564    0.006 layers.py:373(step)
                2492184  190.122    0.000 10602.730    0.004 layers.py:18(step)
                4984368   15.793    0.000 10485.865    0.002 agent.py:26(learn)
              249218400  509.664    0.000 10392.713    0.000 layer.py:74(move)
                4984368  278.472    0.000 8831.219    0.002 learner.py:42(Qlearn)
              249218400  745.633    0.000 8013.113    0.000 layers.py:390(check)
                2492184   78.326    0.000 6268.898    0.003 agent.py:50(_learn)
                2492184 2863.979    0.001 4925.955    0.002 replaybuffer.py:27(teleporter_save_data)
        156999909/17444697  573.365    0.000 4699.574    0.000 module.py:866(_call_impl)
              249218400 4102.010    0.000 4619.313    0.000 layers.py:76(check)
                2492185  248.783    0.000 4466.882    0.002 layers.py:344(update)
               12460329   33.815    0.000 4369.258    0.000 network.py:24(forward)
               12460329  138.055    0.000 4261.726    0.000 container.py:117(forward)
                2492184   68.269    0.000 4191.577    0.002 agent.py:101(_learn)
                2492184 1997.527    0.001 3436.599    0.001 agent.py:77(interveen)
                4984368   37.829    0.000 3429.824    0.001 optimizer.py:84(wrapper)
                4984368   18.651    0.000 3256.587    0.001 grad_mode.py:24(decorate_context)
                4984368  122.987    0.000 3195.213    0.001 adam.py:55(step)
                4984368  661.519    0.000 2919.767    0.001 _functional.py:53(adam)
                4983777  104.219    0.000 2909.460    0.001 agent.py:45(__call__)
                4984368   19.314    0.000 2258.790    0.000 tensor.py:195(backward)
                4984368   17.963    0.000 2238.868    0.000 __init__.py:68(backward)
                4984368 2130.506    0.000 2130.506    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               22429665 1208.618    0.000 1845.681    0.000 layer.py:119(update)
              203507544 1714.741    0.000 1714.741    0.000 {built-in method clone}
                6020112   54.997    0.000 1661.001    0.000 layers.py:394(restart)
                2492184  890.210    0.000 1660.337    0.001 replaybuffer.py:23(sample_data)
              249218400  369.500    0.000 1641.851    0.000 layers.py:384(isFree)
               24920658   58.658    0.000 1612.189    0.000 conv.py:398(forward)
               24920658   30.615    0.000 1531.335    0.000 conv.py:390(_conv_forward)
                2492184  911.972    0.000 1508.938    0.001 agent.py:59(modify)
               24920658 1500.721    0.000 1500.721    0.000 {built-in method conv2d}
             1906237433 1045.078    0.000 1272.351    0.000 layer.py:71(isFree)
               32396619   63.546    0.000 1184.590    0.000 linear.py:93(forward)
               32396619   24.337    0.000 1093.300    0.000 functional.py:1737(linear)
               32396619 1063.138    0.000 1063.138    0.000 {built-in method torch._C._nn.linear}
                6020112   23.436    0.000 1053.460    0.000 level.py:8(__init__)
             4063844216  664.672    0.000  962.764    0.000 enum.py:646(__hash__)
                6020112  146.283    0.000  942.852    0.000 levels.py:95(generate)
                2492184   30.668    0.000  929.450    0.000 agent.py:96(__call__)
                7475961   41.897    0.000  896.526    0.000 agent.py:54(modify_board)
               10632505  762.924    0.000  762.924    0.000 {built-in method tensor}
               22429065  743.014    0.000  743.014    0.000 {built-in method cat}
               44856948   32.389    0.000  629.103    0.000 activation.py:713(forward)
                4984368    4.740    0.000  624.559    0.000 game.py:23(board)
              249218400  383.173    0.000  624.285    0.000 layers.py:216(check)
              249218500   70.491    0.000  616.346    0.000 {built-in method builtins.all}
                2492184   41.560    0.000  607.536    0.000 replaybuffer.py:19(stacker)
              249218400  370.713    0.000  606.096    0.000 layers.py:244(check)
              249218400  365.088    0.000  603.605    0.000 layers.py:230(check)
               44856948   34.823    0.000  596.715    0.000 functional.py:1364(leaky_relu)
                7475961  593.838    0.000  593.838    0.000 {built-in method torch._C._nn.one_hot}
              761974294  171.855    0.000  573.793    0.000 layers.py:350(<genexpr>)
               89718624  555.999    0.000  555.999    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               44856948  555.210    0.000  555.210    0.000 {built-in method torch._C._nn.leaky_relu}
               54181008   74.207    0.000  536.172    0.000 layer.py:48(restart)
               12040224   70.167    0.000  517.064    0.000 level.py:41(notUsed)
               89718624  511.976    0.000  511.976    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4984368   88.946    0.000  510.483    0.000 optimizer.py:189(zero_grad)
             5806153065  496.660    0.000  496.660    0.000 layer.py:67(positions)
              249218400  300.193    0.000  449.380    0.000 layers.py:63(check)
             1694018004  415.309    0.000  415.309    0.000 layer.py:114(elements)
              210983505  396.870    0.000  396.870    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              826223805  287.693    0.000  389.340    0.000 layer.py:98(add)
              249218500  248.761    0.000  380.082    0.000 layers.py:110(isDone)
                8512296  124.293    0.000  346.548    0.000 random.py:315(sample)
              391386306  168.545    0.000  345.383    0.000 layer.py:94(remove)
                2492184  199.186    0.000  340.140    0.000 collector.py:54(collect)
               44859312  336.995    0.000  336.995    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              249218400  194.819    0.000  302.669    0.000 layers.py:203(check)
             4063862543  298.095    0.000  298.095    0.000 {built-in method builtins.hash}
               44859312  293.516    0.000  293.516    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4983777  109.318    0.000  292.784    0.000 exploration.py:53(softmaxer)
                6020212  145.105    0.000  291.140    0.000 layers.py:33(reset)
               44859312  276.445    0.000  276.445    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               44859312  272.183    0.000  272.183    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              301005600  271.734    0.000  271.734    0.000 level.py:32(inverse)
              314015238  192.976    0.000  239.405    0.000 tensor.py:906(grad)
        2614632706/2614632704  170.617    0.000  203.256    0.000 {built-in method builtins.len}
               44859312  200.469    0.000  200.469    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4984368    6.322    0.000  195.076    0.000 loss.py:527(forward)
                4984368   16.885    0.000  188.754    0.000 functional.py:2898(mse_loss)
              249218400   80.291    0.000  177.301    0.000 layers.py:99(<listcomp>)
             1906237433  173.637    0.000  173.637    0.000 layer.py:175(isBlocking)
             2568152674  171.117    0.000  171.117    0.000 {method 'append' of 'list' objects}
              305273888  116.605    0.000  168.846    0.000 random.py:250(_randbelow_with_getrandbits)
               14953104  147.610    0.000  147.610    0.000 {built-in method sum}
              391386306  146.349    0.000  146.349    0.000 {method 'remove' of 'list' objects}
               12040224    9.884    0.000  133.871    0.000 level.py:38(elementsIn)
                4984368  116.256    0.000  116.256    0.000 {built-in method torch._C._nn.mse_loss}
               24920658   15.766    0.000  109.811    0.000 flatten.py:39(forward)
                4985115  107.351    0.000  107.351    0.000 {built-in method max}
                2492184    8.861    0.000  105.854    0.000 exploration.py:47(epsilonGreedy)
                7476552    9.623    0.000  102.246    0.000 tensor.py:525(__rsub__)
               24920658   94.045    0.000   94.045    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4983777   91.994    0.000   91.994    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9444623: <Rock_level_hard_Khigh_0> in cluster <dcc> Done

Job <Rock_level_hard_Khigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:57 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 02:08:58 2021
Terminated at Sun Mar 21 13:04:25 2021
Results reported at Sun Mar 21 13:04:25 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   39213.07 sec.
    Max Memory :                                 5817 MB
    Average Memory :                             4297.36 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2375.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39356 sec.
    Turnaround time :                            39328 sec.

The output (if any) is above this job summary.

