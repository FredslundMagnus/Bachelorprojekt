
# Parameters

    Name :                      Rock_level_hard_epslow-0
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
    K :                         200000
    Epsilon cap :               0.0
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


      38475056972 function calls (38352198101 primitive calls) in 39315.75 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.752 39315.752 {built-in method builtins.exec}
                      1    0.977    0.977 39315.752 39315.752 <string>:1(<module>)
                      1   91.732   91.732 39314.775 39314.775 main.py:13(teleport)
                2193918    8.403    0.000 15691.338    0.007 game.py:27(step)
                2193918   10.569    0.000 15224.039    0.007 layers.py:373(step)
                2193918  174.625    0.000 9553.984    0.004 layers.py:18(step)
              219391800  416.707    0.000 9360.238    0.000 layer.py:74(move)
                4387836   15.748    0.000 9330.339    0.002 agent.py:26(learn)
                4387836  249.937    0.000 7847.895    0.002 learner.py:42(Qlearn)
              219391800  674.847    0.000 7395.849    0.000 layers.py:390(check)
                2193918 3614.866    0.002 6171.914    0.003 replaybuffer.py:27(teleporter_save_data)
                2193919  227.011    0.000 5646.327    0.003 layers.py:344(update)
                2193918   71.422    0.000 5580.525    0.003 agent.py:50(_learn)
              219391800 3739.166    0.000 4256.824    0.000 layers.py:76(check)
        138215157/15357297  519.119    0.000 4192.828    0.000 module.py:866(_call_impl)
               10969461   29.731    0.000 3894.720    0.000 network.py:24(forward)
               10969461  124.023    0.000 3798.619    0.000 container.py:117(forward)
                2193918 2492.334    0.001 3781.698    0.002 agent.py:77(interveen)
                2193918   62.529    0.000 3724.769    0.002 agent.py:101(_learn)
                4387836   35.513    0.000 3047.803    0.001 optimizer.py:84(wrapper)
                4387836   18.504    0.000 2892.463    0.001 grad_mode.py:24(decorate_context)
                4387836  112.605    0.000 2836.370    0.001 adam.py:55(step)
                9886412   83.649    0.000 2697.222    0.000 layers.py:394(restart)
                4387707   94.191    0.000 2601.525    0.001 agent.py:45(__call__)
                4387836  589.598    0.000 2587.165    0.001 _functional.py:53(adam)
              255953814 2097.965    0.000 2097.965    0.000 {built-in method clone}
               19745271 1422.731    0.000 2070.306    0.000 layer.py:119(update)
                4387836   17.065    0.000 1999.782    0.000 tensor.py:195(backward)
                4387836   16.127    0.000 1982.149    0.000 __init__.py:68(backward)
                4387836 1884.800    0.000 1884.800    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9886412   38.159    0.000 1710.938    0.000 level.py:8(__init__)
                9886412  241.293    0.000 1532.038    0.000 levels.py:95(generate)
                2193918  773.861    0.000 1459.201    0.001 replaybuffer.py:23(sample_data)
               21938922   45.685    0.000 1426.049    0.000 conv.py:398(forward)
                2193918  887.524    0.000 1416.805    0.001 agent.py:59(modify)
               21938922   27.677    0.000 1360.748    0.000 conv.py:390(_conv_forward)
              219391800  305.240    0.000 1357.248    0.000 layers.py:384(isFree)
               21938922 1333.071    0.000 1333.071    0.000 {built-in method conv2d}
               28520547   56.176    0.000 1052.921    0.000 linear.py:93(forward)
             1485404617  869.632    0.000 1052.009    0.000 layer.py:71(isFree)
             4068185199  672.560    0.000  976.078    0.000 enum.py:646(__hash__)
               28520547   22.542    0.000  970.789    0.000 functional.py:1737(linear)
               28520547  942.863    0.000  942.863    0.000 {built-in method torch._C._nn.linear}
               88977708  119.646    0.000  875.659    0.000 layer.py:48(restart)
               19772824  109.933    0.000  842.224    0.000 level.py:41(notUsed)
                6581625   39.674    0.000  796.090    0.000 agent.py:54(modify_board)
                2193918   27.213    0.000  788.748    0.000 agent.py:96(__call__)
               19745133  664.399    0.000  664.399    0.000 {built-in method cat}
                8883880  661.456    0.000  661.456    0.000 {built-in method tensor}
              219391800  356.651    0.000  575.608    0.000 layers.py:216(check)
              219391900   62.953    0.000  565.999    0.000 {built-in method builtins.all}
               39490008   32.859    0.000  564.860    0.000 activation.py:713(forward)
              219391800  344.208    0.000  561.763    0.000 layers.py:230(check)
                4387836    4.265    0.000  556.189    0.000 game.py:23(board)
              219391800  342.152    0.000  553.453    0.000 layers.py:244(check)
                2193918   36.175    0.000  539.631    0.000 replaybuffer.py:19(stacker)
               39490008   31.897    0.000  532.001    0.000 functional.py:1364(leaky_relu)
              683842327  159.709    0.000  528.440    0.000 layers.py:350(<genexpr>)
                6581625  522.523    0.000  522.523    0.000 {built-in method torch._C._nn.one_hot}
             1118682899  383.355    0.000  518.200    0.000 layer.py:98(add)
              262535439  494.513    0.000  494.513    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               39490008  493.684    0.000  493.684    0.000 {built-in method torch._C._nn.leaky_relu}
               78981048  493.082    0.000  493.082    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                9886512  237.803    0.000  477.792    0.000 layers.py:33(reset)
                4387836   82.779    0.000  458.929    0.000 optimizer.py:189(zero_grad)
               78981048  452.727    0.000  452.727    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2271901696  448.891    0.000  448.891    0.000 layer.py:114(elements)
             5030561780  448.258    0.000  448.258    0.000 layer.py:67(positions)
              494320600  447.149    0.000  447.149    0.000 level.py:32(inverse)
              219391800  295.978    0.000  442.308    0.000 layers.py:63(check)
               12080330  158.613    0.000  441.832    0.000 random.py:315(sample)
              219391900  232.987    0.000  347.822    0.000 layers.py:110(isDone)
              374855631  165.840    0.000  347.769    0.000 layer.py:94(remove)
                2193918  178.854    0.000  305.401    0.000 collector.py:54(collect)
             4068201366  303.521    0.000  303.521    0.000 {built-in method builtins.hash}
               39490524  300.410    0.000  300.410    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              219391800  178.791    0.000  276.562    0.000 layers.py:203(check)
                4387707   98.909    0.000  262.520    0.000 exploration.py:53(softmaxer)
               39490524  260.536    0.000  260.536    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               39490524  242.265    0.000  242.265    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39490524  238.997    0.000  238.997    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              406342589  156.339    0.000  225.103    0.000 random.py:250(_randbelow_with_getrandbits)
               19772824   15.272    0.000  217.382    0.000 level.py:38(elementsIn)
              276433722  172.660    0.000  214.409    0.000 tensor.py:906(grad)
             3298542121  212.893    0.000  212.893    0.000 {method 'append' of 'list' objects}
        2303733168/2303733166  155.112    0.000  185.426    0.000 {built-in method builtins.len}
               39490524  180.344    0.000  180.344    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              219391800   77.767    0.000  176.621    0.000 layers.py:99(<listcomp>)
                4387836    5.793    0.000  173.429    0.000 loss.py:527(forward)
                4387836   16.317    0.000  167.637    0.000 functional.py:2898(mse_loss)
              374855631  152.561    0.000  152.561    0.000 {method 'remove' of 'list' objects}
             1485404617  137.122    0.000  137.122    0.000 layer.py:175(isBlocking)
               13163508  131.341    0.000  131.341    0.000 {built-in method sum}
               19772824   63.342    0.000  124.033    0.000 level.py:39(<listcomp>)
                9886412   53.462    0.000  114.428    0.000 level.py:16(<dictcomp>)
                4387836  101.922    0.000  101.922    0.000 {built-in method torch._C._nn.mse_loss}
               21938922   16.556    0.000   98.564    0.000 flatten.py:39(forward)
              810694722   96.199    0.000   96.199    0.000 layer.py:150(grid)
                4388493   94.484    0.000   94.484    0.000 {built-in method max}
                6581754    8.367    0.000   89.571    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9444625: <Rock_level_hard_epslow_0> in cluster <dcc> Done

Job <Rock_level_hard_epslow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 02:08:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 02:08:59 2021
Terminated at Sun Mar 21 13:04:26 2021
Results reported at Sun Mar 21 13:04:26 2021

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

    CPU time :                                   39211.72 sec.
    Max Memory :                                 5426 MB
    Average Memory :                             4038.06 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2766.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39356 sec.
    Turnaround time :                            39328 sec.

The output (if any) is above this job summary.

